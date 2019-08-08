    var Position = require('../models/position');

    // Create
    exports.createPosition = function(req, res) {
        var position = new Position(
            {
                account: req.body.account,
                stock: req.body.stock,
                quantity: req.body.quantity,
                price: req.body.price
            }
        );

        position.save(function (err) {
            if (err) {
                return next(err)
            }
            res.send('仓位记录添加成功')
        })
    };

    // Read
    exports.queryPosition = function(req, res) {
        Position.find({account: req.params.account}, function(err, position) {
            if (err) return next(err);
            res.send(position);
        })
    };

    // Update
    exports.updatePosition = function(req, res) {
        Position.findByIdAndUpdate(req.params.id, {$set: req.body}, function(err, position) {
            if (err) next(err);
            res.send('仓位记录更新成功');
        })
    };

    // Delete
    exports.deletePosition = function(req, res) {
        Position.findByIdAndRemove(req.params.id, function(err) {
            if (err) return next(err);
            res.send('仓位记录删除成功');
        })
    };