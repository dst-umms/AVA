var uploadFile = Ext.create('AVA.view.main.UploadFile', {});
var varGrid = Ext.create('AVA.view.main.VariantGrid', {});

Ext.define('AVA.view.main.Main', {
  extend: 'Ext.container.Viewport',
  layout: 'border',
  items: [
    uploadFile,
    varGrid 
  ]
})

varGrid.hide();
