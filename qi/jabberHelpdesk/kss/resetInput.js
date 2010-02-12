
new function () {
kukit.actionsGlobalRegistry.register('jh_resetInput', function (oper) {
;;; oper.componentName = '[jh_resetInput] action';
    
    var node = oper.node;
    node.value = '';
});
kukit.commandsGlobalRegistry.registerFromAction(
    'jh_resetInput', kukit.cr.makeSelectorCommand);
}();
