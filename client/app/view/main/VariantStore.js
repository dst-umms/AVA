Ext.define('AVA.view.main.VariantStore', {
  extend: 'Ext.data.JsonStore',
  storeId: 'var-store',
  model: 'AVA.model.LoadVariants',
  
  proxy: {
    type: 'ajax',
    url: 'http://localhost/server/GetVariantInfo',
    reader: {
      type: 'json',
    }
  },
  autoLoad: false
})
