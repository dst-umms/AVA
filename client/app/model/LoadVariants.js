Ext.define('AVA.model.LoadVariants', {
  extend: 'Ext.data.Model',
  fields: ['Chrom', {
    name: 'Start',
    type: 'int'
  }, 'Ref', 'Alt', "p.gnomad", "c.gnomad", "func.gnomad", "AF.gnomad", "rs.gnomad", "Comments", { 
    name: 'id',
    type: 'int'
  }]
});
