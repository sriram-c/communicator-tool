
;Load user prep file
(defrule load_user_prep_file
(declare (salience 100))
(user_id-chunk-vib ?id ?chunk ?vib)
(not (file_loaded ?id))
=>
	(bind ?file (str-cat ?*prep_prov_path*  ?vib ".clp"))
	(if (neq (load* ?file) FALSE) then
		(assert (file_loaded ?id))
	)
)

;Load original prep file
(defrule load_org_prep_file
(declare (salience -10))
(user_id-chunk-vib ?id ?chunk ?vib)
(not (file_loaded ?id))
 =>
        (bind ?file (str-cat ?*prep_path*  ?vib ".clp"))
        (if (neq (load* ?file) FALSE) then
            (assert (file_loaded ?id))
       )
)

;Prep disambiguation based on verb 
;usane [cunAva_meM] kismawa [AjamAyA]
(defrule disambiguate_using_verb
(declare (salience -500))
(verb-rel-prep ?verb ?rel ?prep) ;verb = AjamA
(user_id-lemma ?h ?lem)  ;lem = AjamA_1
(test (eq (string-to-field (sub-string 1 (- (str-index "_" ?lem) 1) ?lem)) ?verb)) 
(user_inter_chunk_rel-ids ?rel ?h  ?id)
(not (file_loaded ?id))
=>
	 (assert (prep_wrd-ids ?prep ?h ?id))
)


;When there is no user defined prep file or original prep file then get prep from default dic 
(defrule default_rule
(declare (salience -1000))
(user_id-chunk-vib ?id ?chunk ?vib)
(or (user_inter_chunk_rel-ids ?rel ?h  ?id) (user_discourse_rel-ids ?rel ?h  ?id))
;(user_id-cat ?id ?cat&~poss_propn&~poss_n&~poss_pron&~place_adv&~time_adv);[rAma_kA betA] vixyAlaya_meM paDawA_hE. She does not come [here].
(test (eq (gdbm_lookup_p "default_prep.gdbm" ?rel) TRUE))
(not (file_loaded ?id))
=>
	(bind ?prep  (gdbm_lookup "default_prep.gdbm" ?rel))
	(assert (prep_wrd-ids (string-to-field ?prep) ?h ?id))
)
