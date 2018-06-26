Ext.define('AVA.view.main.UploadFile', {
  extend: 'Ext.form.Panel',
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
    allowBlank: false,
    anchor: '100%',
    buttonText: 'Select Variant File ...'
  }],
  buttons: [{
    text: 'Upload',
    handler: function() {
      var form = this.up('form').getForm();
      if(form.isValid()) {
        form.submit({
          url: 'http://localhost:8080/UploadVariantFile',
          waitMsg: 'Uploading Variant File ...',
          success: function(fp, o) {
            Ext.Msg.alert('Success', 'Variant File "' + o.file + '" has been uploaded.');
            var store = Ext.get('var-store');
            store.load();
            store.doLayout();
          }
        });
      }
    }
  }]
})
