//var varStore = Ext.create('AVA.view.main.VariantStore', {});
var data = '[{"name": "Lisa", "email": "lisa@simpsons.com", "phone":"555-111-1224"}, {"name": "Bart", "email":"bart@simpsons.com", "phone":"555-222-1234"}, {"name": "Homer", "email":"home@simpsons.com", "phone":"555-222-1244"}, {"name": "Marge", "email":"marge@simpsons.com", "phone":"555-222-1254"}]';

Ext.define('AVA.view.main.UploadFile', {
  extend: 'Ext.form.Panel',
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
          url: 'photo-upload.php',
          waitMsg: 'Uploading Variant File ...',
          failure: function(fp, o) {
            Ext.Msg.alert('Success', 'Variant File "' + o.result.file + '" has been uploaded.');
            var grid = Ext.getCmp("VarGrid");
            var store = grid.getStore();
            store.loadData(data);
            grid.refresh();
          }
        });
      }
    }
  }]
})
