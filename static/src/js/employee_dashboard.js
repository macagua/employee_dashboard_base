odoo.define('employee_dashboard_base.dashboard', function (require) {
    'use strict';

    console.log('Employee Dashboard Base Module Loaded');

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    // Defines a widget named "EmployeeDashboardBaseAction"
    var EmployeeDashboardBaseAction = AbstractAction.extend({
        // Use "employee_dashboard_base.ClientAction" QWeb template
        template: "employee_dashboard_base.ClientAction",
        init: function () {
            this._super.apply(this, arguments);
            console.log('Employee Dashboard Base Module initialized');
        }
    });

    // Registry "EmployeeDashboardBaseAction" action
    core.action_registry.add('employee_dashboard_base.action', EmployeeDashboardBaseAction);
});

