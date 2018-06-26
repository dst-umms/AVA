var uploadFile = Ext.create('AVA.view.main.UploadFile', {});

Ext.define('AVA.view.main.Main', {
  extend: 'Ext.container.Viewport',
  id: 'center-panel',
  items: [
    uploadFile
  ]
})
