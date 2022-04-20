async function createService(req, res, next) {
  try {
    returnData = [];
    let id = 1;
    req.body.forEach(async (data) => {
      await serviceCodeService.getByServiceCode(data.serviceCode);
      await serviceService.checkPermission("create", req.user);
      let inputs;
      if (req.user.role === Role.Admin) {
        inputs = {
          customerId: data.ownerId || req.user.id,
          ownerId: req.user.id,
          cost: data.cost * 100,
          customerPhone: formatPhone(data.customerPhone),
        };
      } else if (req.user.role === Role.API) {
        inputs = {
          customerId: null,
          ownerId: req.user.id,
          tx: `${req.user.id}-${data.tx}`,
          cost: data.cost * 100,
          location: req.user.location,
          customerPhone: formatPhone(data.customerPhone),
        };
        let service = await serviceService.checkByTx(inputs.tx);
        if (service) {
          let singleResponse = {
            dataId: id,
            status: 0,
            message: "duplicate payment found",
          };

          returnData.push(singleResponse);
        }
      } else {
        inputs = {
          customerId: req.user.id,
          ownerId: req.user.id,
          cost: data.cost * 100,
          customerPhone: formatPhone(data.customerPhone),
        };
      }

      let vehicle = await vehicleService.findByPlateNumberOrCreate(
        data.plateNumber
          .trim()
          .toUpperCase()
          .replace(/[^\w\s]/gi, ""),
        Object.assign({}, data, inputs, {
          plateNumber: data.plateNumber.toUpperCase().replace(/[^\w\s]/gi, ""),
          chassisNumber: data.chassisNumber
            .trim()
            .toUpperCase()
            .replace(/[^\w\s]/gi, ""),
        })
      );
      inputs = Object.assign(
        {},
        data,
        inputs,
        { vehicleId: vehicle ? vehicle.id : null },
        {
          plateNumber: data.plateNumber
            .trim()
            .toUpperCase()
            .replace(/[^\w\s]/gi, ""),
          chassisNumber: data.chassisNumber
            .trim()
            .toUpperCase()
            .replace(/[^\w\s]/gi, ""),
        }
      );
      let response = await serviceService.create(inputs);
      /////////// Update location of vehicle
      if (response.active) {
        await vehicleService.update(vehicle.id, {
          location: req.user.location,
        });
      }
      //////////
      let singleResponse = {
        dataId: id,
        status: 1,
        message: "Received successfuly",
        data: response,
      };

      returnData.push(singleResponse);

      id++;
    });

    return res.json(returnData);
  } catch (err) {
    console.log({ err });
    return next(err.message);
  }
}
