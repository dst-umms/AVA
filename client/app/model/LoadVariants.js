Ext.define('AVA.model.LoadVariants', {
  extend: 'Ext.data.Model',
  fields: ['Chrom', {
    name: 'Start',
    type: 'int'
  }, 'Ref', 'Alt', "p.gnomad", "c.gnomad", "func.gnomad", "AF.gnomad", "rs.gnomad", 
  "c.ALD", "p.ALD", "Exon.ALD", "Remark.ALD"
  , "Comments", { 
    name: 'id',
    type: 'int'
  }]
});
