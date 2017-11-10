(load-facts "mrs_facts.dat")


(defrule proper_q
?f0<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id) 
(test (eq ?name proper_q))
=>
	(retract ?f0)
        (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
)

(defrule named
?f1<-(named-mrs_id-mrs_hndl-CARG ?named ?mrs_id ?hndl ?CARG)
(test (eq ?named named))
=>
       (retract ?f1)
       (assert (named-mrs_id-mrs_hndl-id named_rel ?mrs_id ?hndl ?CARG) )
)
(defrule pronoun_q
?f2<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name pronoun_q))
=>
       (retract ?f2)
       (assert (name-mrs_id-mrs_hndl-id "pronoun_q_rel" ?mrs_id ?hndl ?id) )
)
(defrule which_q
?f3<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name which_q))
=>
       (retract ?f3)
       (assert (name-mrs_id-mrs_hndl-id "wh_q_rel" ?mrs_id ?hndl ?id) )
)
(defrule udef_q
?f4<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name udef_q))
=>
       (retract ?f4)
       (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
)
(defrule udef_q
?f5<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name udef_q))
=>
       (retract ?f5)
       (assert (name-mrs_id-mrs_hndl-id "focus_d_rel" ?mrs_id ?hndl ?id) )
)
(defrule _a_q
?f6<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _a_q))
=>
       (retract ?f6)
       (assert (name-mrs_id-mrs_hndl-id "_ein_q_rel" ?mrs_id ?hndl ?id) )
)
(defrule _the_q
?f7<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _the_q))
=>
       (retract ?f7)
       (assert (name-mrs_id-mrs_hndl-id "_def_q_rel" ?mrs_id ?hndl ?id) )
)
(defrule _for_p
?f8<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _for_p))
=>
       (retract ?f8)
       (assert (name-mrs_id-mrs_hndl-id "_cause_a_rel" ?mrs_id ?hndl ?id) )
)

;(defrule pron_1
;(declare (salience 10))
;?f9<-(pr_mrs_id-pers-Num-Pt ?x_mrs_id ?pers&1|2 ?Num ?Pt)
;?f91<-(name-mrs_id-mrs_hndl-id pron ?x_mrs_id ?hndl ?id)
;=>
 ;       (retract ?f91)
  ;      (assert (name-mrs_id-mrs_hndl-id "pron_n_rel" ?x_mrs_id ?hndl ?id) )
;)

(defrule pron
?f10<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name pron))
=>
       (retract ?f10)
       (assert (name-mrs_id-mrs_hndl-id "_pron_n_ppro_rel" ?mrs_id ?hndl ?id) )
)


(defrule rm_IND
?f11<-(x_mrs_id-pers-Num-Ind ?x_mrs_id ?pers ?Num +)
=>
       (retract ?f11)
       (assert (x_mrs_id-pers-Num-Ind ?x_mrs_id ?pers ?Num) )
)

;(defrule in
;?f10<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
;(test (eq ?name _in_p))
;=>
 ;      (retract ?f10)
  ;     (assert (name-mrs_id-mrs_hndl-id "_in_p_loc_rel" ?mrs_id ?hndl ?id) )
;)

(defrule Tense1
(declare(salience 10))
?f9<-(name-mrs_id-mrs_hndl-id _in_p ?e ?mrs_hndl ?id)
?f91<-(e_mrs_id-SF-Tns-Mood-prog-perf ?e ?SF ?Tns ?Mood ?prog ?perf)
=>
        (retract ?f91)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?e ?SF none) )
)

(defrule Tense2
(declare(salience 10))
?f9<-(name-mrs_id-mrs_hndl-id _on_p e8 ?mrs_hndl ?id)
?f91<-(e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF ?Tns ?Mood ?prog ?perf)
=>
        (retract ?f91)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF none) )
)

(defrule Tense3
(declare(salience 10))
?f9<-(name-mrs_id-mrs_hndl-id _never_a_1 e8 ?mrs_hndl ?id)
?f91<-(e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF ?Tns ?Mood ?prog ?perf)
=>
        (retract ?f91)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF none) )
)

;(defrule default2
;?f14<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
;(test (eq(sub-string(-(length ?name)2)(length ?name)?name)"a_1"))
;
;=>
;      (retract ?f14)
;      
;      (bind ?newname (string-to-field (str-cat (sub-string 1(-(length ?name)1)?name)"rel")))
;      (assert (name-mrs_id-mrs_hndl-id ?newname ?mrs_id ?hndl ?id) )
;)

(defrule to
?f15<-(name-mrs_id-mrs_hndl-id _to_p ?mrs_id ?hndl ?id)
;(test (eq ?name _to_p)
=>
       (retract ?f15)
       (assert (name-mrs_id-mrs_hndl-id "_nach_p_rel" ?mrs_id ?hndl ?id) )
)

(defrule default3
?f11<-(e_mrs_id-SF-Tns-Mood-prog-perf ?e_mrs_id ?SF ?Tns indicative - -)
=>
       (retract ?f11)
       (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?e_mrs_id ?SF ?Tns) )
)

(defrule default4
?f11<-(pr_mrs_id-pers-Num-Pt ?pr_mrs_id ?pers ?Num std)
=>
       (retract ?f11)
       (assert (pr_mrs_id-pers-Num-Pt ?pr_mrs_id ?pers ?Num) )
)

(defrule Tense
?f9<-(name-mrs_id-mrs_hndl-id _to_p e8 ?mrs_hndl ?id)
?f91<-(e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF ?Tns ?Mood ?prog ?perf)
=>
        (retract ?f91)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf e8 ?SF none) )
)

(defrule rm_arg
(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
?f0<-(mrs_id-Args ?mid ?arg)
=>
        (retract ?f0)
        (assert (mrs_id-Args  ?mid ))
)

(defrule mod_tense
(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
?f0<-(e_mrs_id-SF-Tns-Mood-prog-perf   ?mid ?sf untensed ?m ?prog ?perf )
(test (or (eq (sub-string (- (length ?name) 3) (length ?name ) ?name) "_a_1")
          (eq (sub-string (- (length ?name) 3) (length ?name ) ?name) "_p_1"))
)
=>
        (retract ?f0)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf   ?mid ?sf none ?m ?prog ?perf ))
)






  
(facts)
(agenda)
(watch rules)
(watch facts)
(run)
(save-facts "ger_mrs.dat" visible)
(exit)


	 
