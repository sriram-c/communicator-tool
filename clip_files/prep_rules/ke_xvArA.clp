;insertion of 'by'
;rAma_ke_xvArA rAvaNa mArA_gayA_WA
(defrule ke_xvArA_rule
(user_id-chunk-vib ?id ?chunk ?vib)
(user_inter_chunk_rel-ids k1 ?h  ?id)
(test (eq ?vib ke_xvArA))
=>
	(assert (prep_wrd-ids  by ?h ?id))
	(printout prep_fp "(dir_name-file_name-rule_name-prep_wrd-ids  " ?*prep_path* "ke_xvArA.clp	ke_xvArA_rul1   by	"  ?h " " ?id ")" crlf)
)

;insertion of 'with'
;peMcila_ke_xvArA liKawI_hUz
(defrule ke_xvArA_rule1
(user_id-chunk-vib ?id ?chunk ?vib)
(user_inter_chunk_rel-ids k3 ?h  ?id)
(test (eq ?vib ke_xvArA))
=>
        (assert (prep_wrd-ids  with ?h ?id))
	(printout prep_fp "(dir_name-file_name-rule_name-prep_wrd-ids  " ?*prep_path* "ke_xvArA.clp	ke_xvArA_rule1   with	"  ?h " " ?id ")" crlf)
)
