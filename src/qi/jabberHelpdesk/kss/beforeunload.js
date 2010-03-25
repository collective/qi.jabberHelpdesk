
new function () {
var BeforeUnloadBinder = function() {
};

BeforeUnloadBinder.prototype.__bind__ = function(name, func_to_bind, oper) { 
;;; oper.componentName = '[jh-onbeforeunload] event binding'; 
    var self = this; 
    var speed = oper.parms.speed; 
    var f = oper.makeExecuteActionsHook(); 
    func = function(e) { 
        f(); 
    }; 
    window.onbeforeunload = func;
    kukit.ut.registerEventListener(window, 'onbeforeunload', func); 
};


kukit.eventsGlobalRegistry.register('jh', 'onbeforeunload', 
    BeforeUnloadBinder, '__bind__', null);
}();