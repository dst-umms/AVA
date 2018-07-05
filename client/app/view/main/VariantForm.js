Ext.define('AVA.view.main.VariantForm', {
  extend: 'Ext.form.Panel',
  title: 'Variant Form',
  bodyPadding: 5,
  url: 'save-form.php',
  layout: 'anchor',
  defaults: {
    anchor: '100%'
  },
  defaultType: 'textfield',
  items: [{
    fieldLabel: 'First Name',
    name: 'first',
    allowBlank: false
  },{
    fieldLabel: 'Last Name',
    name: 'last',
    allowBlank: false
  }],
  buttons: [{
    text: 'Reset',
    handler: function() {
      this.up('form').getForm().reset();
    }
  }, {
    text: 'Submit',
    formBind: true, //only enabled once the form is valid
    disabled: true,
    handler: function() {
      var form = this.up('form').getForm();
      if (form.isValid()) {
        form.submit({
          success: function(form, action) {
            Ext.Msg.alert('Success', action.result.msg);
          },
          failure: function(form, action) {
            Ext.Msg.alert('Failed', action.result.msg);
          }
        });
      }
    }
  }]
});
