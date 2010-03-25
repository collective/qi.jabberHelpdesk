
new function () {
kukit.actionsGlobalRegistry.register('jh_resetScrollbar', function (oper) {
;;; oper.componentName = '[jh_resetScrollbar] action';
    
    var node = oper.node;
    node.scrollTop = node.scrollHeight
});
kukit.commandsGlobalRegistry.registerFromAction(
    'jh_resetScrollbar', kukit.cr.makeSelectorCommand);
}();
