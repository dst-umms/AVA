var varStore = Ext.create('AVA.view.main.VariantStore', {});

Ext.define('AVA.view.main.VariantGrid', {
  extend: 'Ext.grid.GridPanel',
  id: 'var-grid',
  title: 'Variant-Info',
  store: varStore,
  selModel: 'rowmodel',
  region: 'center',
  columns: [{
      text: '#Chr',
      dataIndex: '#Chr',
      width: 200
    }, { 
    text: 'Start',  
    dataIndex: 'Start', 
    width: 200 
  }, {
    text: 'End',
    dataIndex: 'End',
    width: 200
  },{
    text: 'Ref',
    dataIndex: 'Ref',
    width: 200
  },{
    text: 'Alt',
    dataIndex: 'Alt',
    width: 200
  },{
    text: 'Ref.Gene',
    dataIndex: 'Ref.Gene',
    width: 200
  },{
    text: 'Func.refGene',
    dataIndex: 'Func.refGene',
    width: 200
  },{
    text: 'ExonicFunc.refGene',
    dataIndex: 'ExonicFunc.refGene',
    width: 200
  },{
    text: 'Gene.ensGene',
    dataIndex: 'Gene.ensGene',
    width: 200,
    cellWrap: true
  },{
    text: 'avsnp147',
    dataIndex: 'avsnp147',
    width: 200
  },{
    text: 'AAChange.ensGene',
    dataIndex: 'AAChange.ensGene',
    width: 200,
    cellWrap: true
  },{
    text: 'AAChange.refGene',
    dataIndex: 'AAChange.refGene',
    width: 200,
    cellWrap: true
  },{
    text: 'clinvar: Clinvar',
    dataIndex: 'clinvar: Clinvar ',
    width: 200,
    cellWrap: true
  },{
    text: 'InterVar: InterVar and Evidence',
    dataIndex: ' InterVar: InterVar and Evidence ',
    width: 200,
    cellWrap: true
  },{
    text: 'Freq_ExAC_ALL',
    dataIndex: 'Freq_ExAC_ALL',
    width: 200
  },{
    text: 'Freq_esp6500siv2_all',
    dataIndex: 'Freq_esp6500siv2_all',
    width: 200
  },{
    text: 'Freq_1000g2015aug_all',
    dataIndex: 'Freq_1000g2015aug_all',
    width: 200
  },{
    text: 'CADD_raw',
    dataIndex: 'CADD_raw',
    width: 200
  },{
    text: 'CADD_phred',
    dataIndex: 'CADD_phred',
    width: 200
  },{
    text: 'SIFT_score',
    dataIndex: 'SIFT_score',
    width: 200
  },{
    text: 'GERP++_RS',
    dataIndex: 'GERP++_RS',
    width: 200
  },{
    text: 'phyloP46way_placental',
    dataIndex: 'phyloP46way_placental',
    width: 200
  },{
    text: 'dbscSNV_ADA_SCORE',
    dataIndex: 'dbscSNV_ADA_SCORE',
    width: 200
  },{
    text: 'dbscSNV_RF_SCORE',
    dataIndex: 'dbscSNV_RF_SCORE',
    width: 200
  },{
    text: 'Interpro_domain',
    dataIndex: 'Interpro_domain',
    width: 200,
    cellWrap: true
  },{
    text: 'AAChange.knownGene',
    dataIndex: 'AAChange.knownGene',
    width: 200,
    cellWrap: true
  },{
    text: 'rmsk',
    dataIndex: 'rmsk',
    width: 200,
    cellWrap: true
  },{
    text: 'MetaSVM_score',
    dataIndex: 'MetaSVM_score',
    width: 200
  },{
    text: 'Freq_ExAC_POPs',
    dataIndex: 'Freq_ExAC_POPs',
    width: 200,
    cellWrap: true
  },{
    text: 'OMIM',
    dataIndex: 'OMIM',
    width: 200
  },{
    text: 'Phenotype_MIM',
    dataIndex: 'Phenotype_MIM',
    width: 200,
    cellWrap: true
  },{
    text: 'OrphaNumber',
    dataIndex: 'OrphaNumber',
    width: 200
  },{
    text: 'Orpha',
    dataIndex: 'Orpha',
    width: 200,
    cellWrap: true
  },{
    text: 'Otherinfo',
    dataIndex: 'Otherinfo',
    width: 200,
    cellWrap: true
  }, {
    text: 'id',
    dataIndex: 'id',
    hidden: true
  }],
  listeners: {
    'rowclick': function(grid, record, elem, rowIndex) {
      console.log(record.data);
      var varPanel = Ext.create('AVA.view.main.VariantForm', {});
      var varWindow = Ext.create('Ext.window.Window', {
        id: 'variant-win',
        title: 'Variant-Form:',
        scrollable: true,
        plain:true,
        layout: 'fit',
        items: varPanel,
        height: '100%',
        width: '100%'
      });
      varPanel.getForm().loadRecord(record);
      varWindow.show(); 
    }
  }
});
