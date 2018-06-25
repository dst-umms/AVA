Ext.define('AVA.view.main.VariantStore', {
  extend: 'Ext.data.Store',
  fields: ['name', 'email', 'phone'],
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
})
