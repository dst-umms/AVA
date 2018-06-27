var varStore = Ext.create('AVA.view.main.VariantStore', {});

Ext.define('AVA.view.main.VariantGrid', {
  extend: 'Ext.grid.GridPanel',
  id: 'var-grid',
  title: 'Variant-Info',
  store: varStore,
  region: 'center',
  columns: [{ 
    text: 'Name',  
    dataIndex: 'name', 
    width: 200 
  }, { 
    text: 'Email', 
    dataIndex: 'email', 
    width: 250 
  }, { 
    text: 'Phone', 
    dataIndex: 'phone', 
    width: 120 
  }],
  height: 200,
  layout: 'fit',
  fullscreen: true
})
