Ext.define('AVA.model.LoadVariants', {
  extend: 'Ext.data.Model',
  fields: ['#Chr', {
    name: 'Start',
    type: 'int'
  }, {
    name: 'End',
    type: 'int'
  },
    'Ref', 'Alt', 'Ref.Gene', 'Func.refGene',
    'ExonicFunc.refGene', 'Gene.ensGene', 'avsnp147', 'AAChange.ensGene',
    'AAChange.refGene', 'clinvar: Clinvar ',
    ' InterVar: InterVar and Evidence ', 'Freq_ExAC_ALL',
    'Freq_esp6500siv2_all', 'Freq_1000g2015aug_all', 'CADD_raw',
    'CADD_phred', 'SIFT_score', 'GERP++_RS', 'phyloP46way_placental',
    'dbscSNV_ADA_SCORE', 'dbscSNV_RF_SCORE', 'Interpro_domain',
    'AAChange.knownGene', 'rmsk', 'MetaSVM_score', 'Freq_ExAC_POPs', 'OMIM',
    'Phenotype_MIM', 'OrphaNumber', 'Orpha', 'Otherinfo', {
    name: 'id',
    type: 'int'
  }]
});
