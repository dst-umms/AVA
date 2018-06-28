Ext.define('User', {
  extend: 'Ext.data.Model',
  fields: ['id', 'name']
});

Ext.define('AVA.view.main.VariantStore', {
  extend: 'Ext.data.JsonStore',
  storeId: 'var-store',
  model: 'User',
  
  proxy: {
    type: 'ajax',
    url: 'http://localhost/server/GetJson',
    reader: {
      type: 'json',
    }
  },
  autoLoad: false
})
