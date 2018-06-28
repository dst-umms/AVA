var varStore = Ext.create('AVA.view.main.VariantStore', {});

Ext.define('AVA.view.main.VariantGrid', {
  extend: 'Ext.grid.GridPanel',
  id: 'var-grid',
  title: 'Variant-Info',
  store: varStore,
  region: 'center',
  columns: [{
      text: 'id',
      dataIndex: 'id',
      width: 200
    }, { 
    text: 'Name',  
    dataIndex: 'name', 
    width: 200 
  }]//,
  //height: 200,
  //layout: 'fit',
  //fullscreen: true
})
