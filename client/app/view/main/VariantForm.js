Ext.define('AVA.view.main.VariantForm', {
  extend: 'Ext.form.Panel',
  bodyPadding: 5,
  scrollable: true,
  layout: 'anchor',
  defaults: {
    anchor: '100%',
    xtype: 'textfield',
    labelWidth: 200
  }, 
  items: [{
    name: 'Chrom',
    fieldLabel: 'Chrom',
    allowBlank: false
  },{
    name: 'Start',
    fieldLabel: 'Start',
    allowBlank: false
  }, {
    name: 'Ref',
    fieldLabel: 'Ref',
    allowBlank: false
  }, {
    name: 'Alt',
    fieldLabel: 'Alt',
    allowBlank: false
  }, {
    name: 'p.gnomad',
    fieldLabel: 'p.gnomad',
    allowBlank: false
  }, {
    name: 'c.gnomad',
    fieldLabel: 'c.gnomad',
    allowBlank: false
  }, {
    name: 'func.gnomad',
    fieldLabel: 'func.gnomad',
    allowBlank: false
  }, {
    name: 'AF.gnomad',
    fieldLabel: 'AF.gnomad',
    allowBlank: false
  }, {
    name: 'rs.gnomad',
    fieldLabel: 'rs.gnomad',
    allowBlank: false
  }, {
    name: 'c.ALD',
    fieldLabel: 'c.ALD',
    allowBlank: false
  }, {
    name: 'p.ALD',
    fieldLabel: 'p.ALD',
    allowBlank: false
  }, {
    name: 'Exon.ALD',
    fieldLabel: 'Exon.ALD',
    allowBlank: false
  }, {
    name: 'Remark.ALD',
    fieldLabel: 'Remark.ALD',
    allowBlank: false
  }, {
    name: 'clinvar.HGVS',
    fieldLabel: 'clinvar.HGVS',
    allowBlank: false
  }, {
    name: 'clinvar.SIG',
    fieldLabel: 'clinvar.SIG',
    allowBlank: false
  }, {
    name: 'clinvar.MC',
    fieldLabel: 'clinvar.MC',
    allowBlank: false
  }, {
    name: 'clinvar.RS',
    fieldLabel: 'clinvar.RS',
    allowBlank: false
  }, {
    name: 'Comments',
    fieldLabel: 'Comments',
    allowBlank: false
  }, {
    name: 'id',
    hidden: true
  }],
  buttons: [{
    text: 'Cancel',
    handler: function() {
      Ext.getCmp('variant-win').destroy();
    }
  }, {
    text: 'Update',
    formBind: true, //only enabled once the form is valid
    disabled: true,
    handler: function() {
      var form = this.up('form').getForm();
      if (form.isValid()) {
        var record = form.getRecord();
        record.set(form.getValues());
        Ext.getCmp('var-grid').store.sync();
        Ext.getCmp('variant-win').destroy();
      }
    }
  }]
});
