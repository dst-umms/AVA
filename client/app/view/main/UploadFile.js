Ext.define('AVA.view.main.UploadFile', {
  extend: 'Ext.form.Panel',
  id: 'north-panel',
  region: 'north',
  title: 'Upload variant file',
  //width: 800,
  bodyPadding: 10,
  frame: true,
  items: [{
    xtype: 'filefield',
    name: 'VariantFile',
    fieldLabel: 'variant-file',
    labelWidth: 50,
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
          msg : 'Running Variant Annotation Pipeline.',
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
            console.log(response.result.file);
            var grid = Ext.getCmp('var-grid');
            grid.store.load();
            grid.updateLayout();
            grid.show();
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
