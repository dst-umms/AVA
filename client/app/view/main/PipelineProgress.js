
Ext.define('AVA.view.main.PipelineProgress', {
  extend: 'Ext.util.TaskRunner',
  fileIdleEvent: false,
  clearPrototypeOnDestroy: true,
  updateStatus: function() {
    Ext.MessageBox.close();
    Ext.MessageBox.show({
      msg : 'Running Variant Annotation Pipeline.',
      progressText : 'Please wait ...',
      width : 300,
      wait: true
    });
    Ext.Ajax.request({
      url: 'http://localhost/server/PipelineStatus',
      method: 'POST',
      params: {
        proj_name: this.projName,
        task: this.task
      },
      success: function(response, opts) {
        var obj = Ext.decode(response.responseText);
        var progress = obj.status;
        Ext.MessageBox.updateProgress(progress, progress + " % done ...");
        if (progress == 0) {
          Ext.util.TaskManager.stop(opts.params.task);
          Ext.MessageBox.close();
          Ext.Msg.alert('INFO', obj.error);
        }
        if (progress == 100) {
          Ext.util.TaskManager.stop(opts.params.task);
          Ext.MessageBox.close();
          var grid = Ext.getCmp('var-grid');
          grid.store.load({
            params: {
              proj_name: opts.params.proj_name
            }
          });
          grid.updateLayout();
          grid.show();
        }
      },
      failure: function(response, opts) {
        Ext.util.TaskManager.stop(opts.params.task);
        Ext.MessageBox.close();
        console.log('server-side failure with status code ' + response.status);
      }
    });
  },
  projName: undefined,
  task: undefined
})
