var varStore = Ext.create('AVA.view.main.VariantStore', {});

Ext.define('AVA.view.main.VariantGrid', {
  extend: 'Ext.grid.GridPanel',
  id: 'var-grid',
  title: 'Variant-Info',
  store: varStore,
  selModel: 'rowmodel',
  region: 'center',
  columns: [{
      text: 'Chrom',
      dataIndex: 'Chrom',
      width: 200
    }, { 
    text: 'Start',  
    dataIndex: 'Start', 
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
    text: 'p.gnomad',
    dataIndex: 'p.gnomad',
    width: 200
  },{
    text: 'c.gnomad',
    dataIndex: 'c.gnomad',
    width: 200
  },{
    text: 'func.gnomad',
    dataIndex: 'func.gnomad',
    width: 200
  },{
    text: 'AF.gnomad',
    dataIndex: 'AF.gnomad',
    width: 200
  }, {
    text: 'c.ALD',
    dataIndex: 'c.ALD',
    width: 200
  }, {
    text: 'p.ALD',
    dataIndex: 'p.ALD',
    width: 200
  }, {
    text: 'Exon.ALD',
    dataIndex: 'Exon.ALD',
    width: 200
  }, {
    text: 'Remark.ALD',
    dataIndex: 'Remark.ALD',
    width: 200
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
