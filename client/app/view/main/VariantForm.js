Ext.define('AVA.view.main.VariantForm', {
  extend: 'Ext.form.Panel',
  bodyPadding: 5,
  url: 'save-form.php',
  scrollable: true,
  layout: 'anchor',
  defaults: {
    anchor: '100%',
    xtype: 'textfield',
    labelWidth: 200
  }, 
  items: [{
    name: '#Chr',
    fieldLabel: '#Chr',
    allowBlank: false
  },{
    name: 'Start',
    fieldLabel: 'Start',
    allowBlank: false
  }, {
    name: 'End',
    fieldLabel: 'End',
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
    name: 'Ref.Gene',
    fieldLabel: 'Ref.Gene'
  }, {
    name: 'Func.refGene',
    fieldLabel: 'Func.refGene'
  }, {
    name: 'ExonicFunc.refGene',
    fieldLabel: 'ExonicFunc.refGene'
  }, {
    name: 'Gene.ensGene',
    fieldLabel: 'Gene.ensGene'
  }, {
    name: 'avsnp147',
    fieldLabel: 'avsnp147'
  }, {
    name: 'AAChange.ensGene',
    fieldLabel: 'AAChange.ensGene'
  }, {
    name: 'AAChange.refGene',
    fieldLabel: 'AAChange.refGene'
  }, {
    name: 'clinvar: Clinvar ',
    fieldLabel: 'clinvar: Clinvar'
  }, {
    name: ' InterVar: InterVar and Evidence ',
    fieldLabel: 'InterVar: InterVar and Evidence'
  }, {
    name: 'Freq_ExAC_ALL',
    fieldLabel: 'Freq_ExAC_ALL'
  }, {
    name: 'Freq_esp6500siv2_all',
    fieldLabel: 'Freq_esp6500siv2_all'
  }, {
    name: 'Freq_1000g2015aug_all',
    fieldLabel: 'Freq_1000g2015aug_all'
  }, {
    name: 'CADD_raw',
    fieldLabel: 'CADD_raw'
  }, {
    name: 'CADD_phred',
    fieldLabel: 'CADD_phred'
  }, {
    name: 'SIFT_score',
    fieldLabel: 'SIFT_score'
  }, {
    name: 'GERP++_RS',
    fieldLabel: 'GERP++_RS'
  }, {
    name: 'phyloP46way_placental',
    fieldLabel: 'phyloP46way_placental'
  }, {
    name: 'dbscSNV_ADA_SCORE',
    fieldLabel: 'dbscSNV_ADA_SCORE'
  }, {
    name: 'dbscSNV_RF_SCORE',
    fieldLabel: 'dbscSNV_RF_SCORE'
  }, {
    name: 'Interpro_domain',
    fieldLabel: 'Interpro_domain'
  }, {
    name: 'AAChange.knownGene',
    fieldLabel: 'AAChange.knownGene'
  }, {
    name: 'rmsk',
    fieldLabel: 'rmsk'
  }, {
    name: 'MetaSVM_score',
    fieldLabel: 'MetaSVM_score'
  }, {
    name: 'Freq_ExAC_POPs',
    fieldLabel: 'Freq_ExAC_POPs'
  }, {
    name: 'OMIM',
    fieldLabel: 'OMIM'
  }, {
    name: 'Phenotype_MIM',
    fieldLabel: 'Phenotype_MIM'
  }, {
    name: 'OrphaNumber',
    fieldLabel: 'OrphaNumber'
  }, {
    name: 'Orpha',
    fieldLabel: 'Orpha'
  }, {
    name: 'Otherinfo',
    fieldLabel: 'Otherinfo'
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
