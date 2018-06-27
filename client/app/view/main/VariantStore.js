Ext.define('AVA.view.main.VariantStore', {
  extend: 'Ext.data.JsonStore',
  storeId: 'var-store',
  proxy: {
    type: 'ajax',
    url: 'http://localhost/server/GetJson',
    reader: {
      type: 'json',
      rootProperty: 'data'
    }
  },
  fields: ['name', 'email', 'phone'],
  autoLoad: false,
/*
  data: [{ 
    'name': 'Lisa',  
    "email":"lisa@simpsons.com",  
    "phone":"555-111-1224"  
  }, { 
    'name': 'Bart',  
    "email":"bart@simpsons.com",  
    "phone":"555-222-1234" 
  }, { 
    'name': 'Homer', 
    "email":"home@simpsons.com",  
    "phone":"555-222-1244"  
  }, { 
    'name': 'Marge', 
    "email":"marge@simpsons.com", 
    "phone":"555-222-1254"  
  }]
*/
  listeners: {
    load: function(){
      console.log('data loaded');
    }
  }
})
