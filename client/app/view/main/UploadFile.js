var fileTypes = Ext.create('Ext.data.Store', {
  fields: ['abbr', 'name'],
  data : [{
    "format": "txt",
    "name": "Annovar (.txt)"
  }, {
    "format": "vcf", 
    "name": "VCF (.vcf)"
  }, {
    "format": "csv", 
    "name": "NENBSS (.csv)"
  }]
});

Ext.define('AVA.view.main.UploadFile', {
  extend: 'Ext.form.Panel',
  id: 'north-panel',
  collapsible: true,
  region: 'north',
  title: 'Upload variant file',
  //width: 800,
  bodyPadding: 10,
  frame: true,
  items: [{
    xtype: 'combobox',
    fieldLabel: 'file-format',
    name: 'file-format',
    store: fileTypes,
    value: "vcf",
    queryMode: 'local',
    displayField: 'name',
    valueField: 'format',
    labelWidth: 100,
    anchor: '50%',
    allowBlank: false
  }, {
    xtype: 'filefield',
    name: 'VariantFile',
    fieldLabel: 'variant-file',
    labelWidth: 100,
    msgTarget: 'side',
    waitTitle:"test upload message",
    allowBlank: false,
    anchor: '100%',
    buttonText: 'Select Variant File ...'
  }],
  buttons: [{
    text: 'Upload',
    handler: function() {
      var form = this.up('form').getForm();
      if(form.isValid()) {
        Ext.MessageBox.show({
          msg : 'Uploading file.',
          progressText : 'Please wait ...',
          width : 300,
          wait : true,
          waitConfig : {
            duration : 10000,
            increment : 15,
            text : 'Please wait ...',
            scope : this,
            fn : function(obj) {
              obj.restore();   
            }
          }
        });
        form.submit({
          url: 'http://localhost/server/UploadVariantFile',
          success: function(action, response) {
            Ext.MessageBox.close();
            var projName = response.result.file;
            var runner = Ext.create('AVA.view.main.PipelineProgress', {
              projName: projName
            });
            Ext.MessageBox.show({msg: "Launching pipeline", wait: true});
            var grid = Ext.getCmp('var-grid');
            if (grid.isHidden() === false) {
              grid.hide();
            }
            var task = runner.start({
              scope: runner,
              run: runner.updateStatus,
              interval: 10000
            });
            runner.task = task;
          },
          failure: function(action, response) {
            Ext.MessageBox.close();
            console.log("failure");
            console.log(response);
          }
        });
      }
    } 
  }]
})
