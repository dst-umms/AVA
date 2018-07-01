
Ext.define('AVA.view.main.PipelineProgress', {
  extend: 'Ext.util.TaskRunner',
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
        proj_name: this.projName
      },
      success: function(response, opts) {
        var obj = Ext.decode(response.responseText);
        this.progress = obj.status;
        Ext.MessageBox.updateProgress(this.progress, this.progress + " % done ...");
        if (this.progress == 100) {
          Ext.util.TaskManager.destroy();
          Ext.MessageBox.close();
          var grid = Ext.getCmp('var-grid');
          grid.store.load();
          grid.updateLayout();
          grid.show();
        }
      },
      failure: function(response, opts) {
        this.task.stop();
        Ext.MessageBox.close();
        console.log('server-side failure with status code ' + response.status);
      }
    });
  },
  progress: 0,
  projName: undefined,
  task: undefined
})
