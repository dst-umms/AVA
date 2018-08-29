var varStore = Ext.create('AVA.view.main.VariantStore', {});

Ext.define('AVA.view.main.VariantGrid', {
  extend: 'Ext.grid.GridPanel',
  id: 'var-grid',
  title: 'Variant-Info',
  store: varStore,
  selModel: 'rowmodel',
  region: 'center',
  columns: [{
      text: 'Chr',
      dataIndex: 'Chrom',
      width: 50
    }, { 
    text: 'Start',  
    dataIndex: 'Start', 
    width: 100 
  },{
    text: 'Ref',
    dataIndex: 'Ref',
    width: 50
  },{
    text: 'Alt',
    dataIndex: 'Alt',
    width: 50
  },{
    text: 'p.gnomad',
    dataIndex: 'p.gnomad',
    width: 150
  },{
    text: 'c.gnomad',
    dataIndex: 'c.gnomad',
    width: 150
  },{
    text: 'func.gnomad',
    dataIndex: 'func.gnomad',
    width: 150
  },{
    text: 'AF.gnomad',
    dataIndex: 'AF.gnomad',
    width: 100
  }, {
    text: 'c.ALD',
    dataIndex: 'c.ALD',
    width: 150
  }, {
    text: 'p.ALD',
    dataIndex: 'p.ALD',
    width: 150
  }, {
    text: 'Exon.ALD',
    dataIndex: 'Exon.ALD',
    width: 100
  }, {
    text: 'Remark.ALD',
    dataIndex: 'Remark.ALD',
    width: 150
  }, {
    text: 'clinvar.HGVS',
    dataIndex: 'clinvar.HGVS',
    width: 150
  }, {
    text: 'clinvar.SIG',
    dataIndex: 'clinvar.SIG',
    width: 150
  }, {
    text: 'clinvar.MC',
    dataIndex: 'clinvar.MC',
    width: 150
  }, {
    text: 'clinvar.RS',
    dataIndex: 'clinvar.RS',
    width: 150
  }, {
    text: 'dbsnp.RS',
    dataIndex: 'dbsnp.RS',
    width: 150
  }, {
    text: 'dbsnp.AF',
    dataIndex: 'dbsnp.AF',
    width: 150
  }, {
    text: 'Comments',
    dataIndex: 'Comments',
    hidden: true
  }, {
    text: 'id',
    dataIndex: 'id',
    hidden: true
  }],
  listeners: {
    'rowclick': function(grid, record, elem, rowIndex) {
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
