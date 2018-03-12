(load-facts "mrs_facts.dat")
(assert (default_line))

;I live in "Germany".
;"Tom" slept.
(defrule proper_q
?f0<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id) 
(test (eq ?name proper_q))
=>
	(retract ?f0)
        (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
)

;I live in "Germany".
;"Tom" owns a car.
(defrule named
?f1<-(named-mrs_id-mrs_hndl-CARG ?named ?mrs_id ?hndl ?CARG)
(test (eq ?named named))
=>
       (retract ?f1)
       (assert (named-mrs_id-mrs_hndl-id named_rel ?mrs_id ?hndl ?CARG) )
)

;"He" is a thief.
;"He" laughs.
(defrule pronoun_q
?f2<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name pronoun_q))
=>
       (retract ?f2)
       (assert (name-mrs_id-mrs_hndl-id "pronoun_q_rel" ?mrs_id ?hndl ?id) )
)

;He came "yesterday".
(defrule time
?f22<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name time_n))
=>
       (retract ?f22)
       (assert ())
)

;(defrule loc
;?f23<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
;(test (eq ?name loc_nonsp))
;=>
;      (retract ?f23)
;     (assert (name-mrs_id-mrs_hndl-id "unspec_loc_rel" ?mrs_id ?hndl ?id) )
;)

(defrule place
?f24<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name place_n))
=>
       (retract ?f24)
       (assert (name-mrs_id-mrs_hndl-id "place_rel" ?mrs_id ?hndl ?id) )
)

(defrule poss
?f24<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name poss))
=>
       (retract ?f24)
       (assert (name-mrs_id-mrs_hndl-id "poss_rel" ?mrs_id ?hndl ?id) )
)

(defrule poss_tense
(declare (salience 100))
?f241<-(name-mrs_id-mrs_hndl-id poss ?mid ?hndl ?id)
?f242<-(e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf untensed $?p ) 
=>
       (retract ?f242)
       (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf none $?p ) )
)


(defrule card_rel
?f26<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name card))
=>
       (retract ?f26)
       (assert (name-mrs_id-mrs_hndl-id card_rel ?mrs_id ?hndl ?id) )
)


(defrule loc_Tns
(declare (salience 100))
?f25<-(name-mrs_id-mrs_hndl-id loc_nonsp ?mid ?hndl ?id)
?f251<-(e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf untensed ?m ?prog ?perf )
=>
       (retract ?f251)
       (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf none ) )
)


(defrule udef_q
?f4<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name udef_q))
=>
       (retract ?f4)
       (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
)


;(defrule def_explicit_q
;?f4<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
;(test (eq ?name def_explicit_q))
;=>
;      (retract ?f4)
;     (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
;)



;(defrule udef_q
;?f5<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
;(test (eq ?name udef_q))
;=>
;      (retract ?f5)
;     (assert (name-mrs_id-mrs_hndl-id "focus_d_rel" ?mrs_id ?hndl ?id) )
;)

;Tom owns "a" car.
;I am "a" good doctor.
(defrule _a_q
?f6<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _a_q))
=>
       (retract ?f6)
       (assert (name-mrs_id-mrs_hndl-id "_ein_q_rel" ?mrs_id ?hndl ?id) )
)

;"The" boy eats a red apple.
;She sits on "the" chair.
(defrule _the_q
?f7<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _the_q))
=>
       (retract ?f7)
       (assert (name-mrs_id-mrs_hndl-id "_def_q_rel" ?mrs_id ?hndl ?id) )
)

;He bought a pen "for" writing.
(defrule _for_p
?f42<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _for_p))
=>
       (retract ?f42)
       (assert (name-mrs_id-mrs_hndl-id "_zu_p_rel" ?mrs_id ?hndl ?id) )
)

;He came "from" Germany.
(defrule _from_p_dir
?f43<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _from_p_dir))
=>
       (retract ?f43)
       (assert (name-mrs_id-mrs_hndl-id "udef_q_rel" ?mrs_id ?hndl ?id) )
)

;I went "to" Germany.
(defrule _to_p
?f43<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _to_p))
=>
       (retract ?f43)
       (assert (name-mrs_id-mrs_hndl-id "_nach_p_rel" ?mrs_id ?hndl ?id) )
)

(defrule person
?f60<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name person))
=>
       (retract ?f60)
       (assert (name-mrs_id-mrs_hndl-id "abstr_nom_rel" ?mrs_id ?hndl ?id) )
)

(defrule _about_p
?f46<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _about_p))
=>
       (retract ?f46)
       (assert (name-mrs_id-mrs_hndl-id "_ueber_p_loc_rel" ?mrs_id ?hndl ?id) )
)

(defrule _with_p
?f47<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _with_p))
=>
       (retract ?f47)
       (assert (name-mrs_id-mrs_hndl-id "_mit_p_rel" ?mrs_id ?hndl ?id) )
)

(defrule _such_a_1
?f42<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _such_a_1))
=>
       (retract ?f42)
       (assert (name-mrs_id-mrs_hndl-id "_solch_a_rel" ?mrs_id ?hndl ?id) )
)


;"I" went to Germany.
;"He" laughs.
(defrule pron
?f10<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name pron))
=>
       (retract ?f10)
       (assert (name-mrs_id-mrs_hndl-id "_pron_n_ppro_rel" ?mrs_id ?hndl ?id) )
)

;I went to "Germany".
;The boy eats a red "apple".
(defrule rm_IND
?f11<-(x_mrs_id-pers-Num-Ind ?x_mrs_id ?pers ?Num +)
=>
       (retract ?f11)
       (assert (x_mrs_id-pers-Num-Ind ?x_mrs_id ?pers ?Num) )
)


;I "went" to Germany.
;I "will" go.
(defrule default3
?f9<-(e_mrs_id-SF-Tns-Mood-prog-perf ?e_mrs_id ?SF ?Tns indicative ?p ?pe)
=>
       (retract ?f9)
       (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?e_mrs_id ?SF ?Tns) )
)

;"I" went to Germany.
;"Tom" operates a school.
(defrule default4
?f12<-(pr_mrs_id-pers-Num-Pt ?pr_mrs_id ?pers ?Num std)
=>
       (retract ?f12)
       (assert (pr_mrs_id-pers-Num-Pt ?pr_mrs_id ?pers ?Num) )
)

;I am a "good" doctor.
;The girl is "making" a doll.
(defrule rm_arg
;(declare (salience -5))
?f17<-(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
;?f172<-(name-mrs_id-mrs_hndl-id ?name1 ?mid1 ?m_hid ?id )
?f171<-(mrs_id-Args ?mid $?pre ?arg $?post)
(test (or (eq (sub-string 1 1 ?arg) "i")
	  (eq (sub-string 1 1 ?arg) "p")
	  (eq (sub-string 1 1 ?arg) "u")))
=>
        	(retract ?f171)
        	(assert (mrs_id-Args ?mid $?pre $?post ))

)





;(defrule rm_arg1
;?f27<-(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
;?f37<-((ltop-index ?h0 ?e2 )
;;?f272<-(name-mrs_id-mrs_hndl-id ?name1 ?mid1 ?m_hid ?id )
;;?f271<-(mrs_id-Args ?mid $?pre ?arg $?post)
;?f371<-(mrs_id-Args  ?e2 $?pre ?arg2 $?post )
;(test (eq ?name parg_d))
;=>
;
;	(retract ?f371)
 ;       (assert (mrs_id-Args ?e2 $?pre ?arg2 $?post ))
		

        
;)

;(test (neq ?name1 parg_d)
;=>
 ;      (retract ?f171)
  ;     (assert (mrs_id-Args ?mid $?pre $?post ))
   ;    )







;I live "in" Germany.
;He came "from" Germany.
;The carpenter has made a "beautiful" chair.
(defrule mod_tense
(declare (salience 100))
?f14<-(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
?f13<-(e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf untensed $?p1)
(test (or (neq (str-index "_a" ?name) FALSE)
          (neq (str-index "_p" ?name) FALSE))
)
=>
        (retract ?f13)
        (assert (e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf none $?p1))
)

;The morning is "clear".
;The cake is "delicious".
(defrule stat
(declare (salience 100))
?f182<-(ltop-index ?h ?mid)
?f18<-(name-mrs_id-mrs_hndl-id  ?name ?mid ?m_hid ?id )
?f181<-(e_mrs_id-SF-Tns-Mood-prog-perf ?mid ?sf ?Tns $?p1)
(test (or (neq (str-index "_a_" ?name) FALSE)
          (neq (str-index "_p_" ?name) FALSE))
)
=>
        (retract ?f181)
        (assert (e_mrs_id-SF-Tns-STAT   ?mid ?sf ?Tns +))
)

;I "am" a good doctor.
;He "is" a theif.
(defrule stat2
?f212<-(ltop-index ?h ?mid)
?f21<-(name-mrs_id-mrs_hndl-id  _be_v_id ?mid ?m_hid ?id )
?f211<-(e_mrs_id-SF-Tns-Mood-prog-perf   ?mid ?sf ?Tns ?m ?prog ?perf )


=>
        (retract ?f211)
        (assert (e_mrs_id-SF-Tns-STAT   ?mid ?sf ?Tns +))
)


;The boy eats an apple "in" the market.
(defrule _in_p
?f40<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _in_p))
=>
       (retract ?f40)
       (assert (name-mrs_id-mrs_hndl-id "_in_p_loc_rel" ?mrs_id ?hndl ?id) )
)
;He cannot swim.
;He was "not" running.
(defrule neg
?f48<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name neg))
=>
       (retract ?f48)
       (assert (name-mrs_id-mrs_hndl-id "_neg_a_rel" ?mrs_id ?hndl ?id) )
)


(defrule _into_p
?f49<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _into_p))
=>
       (retract ?f49)
       (assert (name-mrs_id-mrs_hndl-id "_in_p_dir_rel" ?mrs_id ?hndl ?id) )
)


(defrule parg_d
?f50<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name parg_d))
=>
       (retract ?f50)
       (assert (name-mrs_id-mrs_hndl-id parg_d_rel ?mrs_id ?hndl ?id) )
)



(defrule _by_p
?f52<-(name-mrs_id-mrs_hndl-id ?name ?mrs_id ?hndl ?id)
(test (eq ?name _by_p))
=>
       (retract ?f52)
       (assert (name-mrs_id-mrs_hndl-id "_von_p_rel" ?mrs_id ?hndl ?id) )
)

;(defrule defaultin
;(declare (salience -1))
;(default_line)
;?f100<-(ltop-index ?h0 ?mrs_id)
;?f101<-(name-mrs_id-mrs_hndl-id  ?name ?mrs_id ?hndl ?id)
;?f202<-(mrs_id-Args  ?mrs_iid ?mrs_id ?iid)
;?f203<-(name-mrs_id-mrs_hndl-id  ?name1 ?mrs_iid ?hndl ?id)
;;(test (eq ?e2 ?mrs_id))
;;(not (added_line))
;=>
;;	(assert (added_line))
;	(if (eq ?name1 parg_d) then
;	(assert (topic-or-focus_d_rel<-1:-1> LBL: ?hndl ARG1: ?mrs_id ARG0: e22 ))
;	else
;	(assert (topic-or-focus_d_rel<-1:-1> LBL: ?hndl ARG1: ?mrs_id ARG0: e22 ARG2: ?iid ))
;	)
;)


(defrule defaultin1
(declare (salience -2))
(default_line)
?f200<-(ltop-index ?h0 ?e2)
?f201<-(name-mrs_id-mrs_hndl-id  ?name ?mrs_id ?hndl ?id)
;?f202<-(mrs_id-Args  ?e10 ?mrs_id ?iid)
;?f203<-(name-mrs_id-mrs_hndl-id  ?name1 ?mrs_iid ?hndl ?id1)
(test (eq ?e2 ?mrs_id))
;;(not (added_line))
=>
; ;      (assert (added_line))
	 (assert (topic-or-focus_d_rel<-1:-1> LBL: ?hndl ARG1: ?mrs_id ARG0: e22 ))
)

(defrule pargdef
(declare (salience -1))
(default_line)
?f300<-(ltop-index ?h0 ?e2)
?f301<-(name-mrs_id-mrs_hndl-id ?name ?e2 ?hndl ?id)
?f302<-(name-mrs_id-mrs_hndl-id ?name1 ?mrs_id ?hndl ?id1)
(test (eq ?name1 parg_d))
=>
	(assert (topic-or-focus_d_rel<-1:-1> LBL:  ARG1:  ARG0: e22 ARG2:  ) )
)
  
(facts)
(agenda)
(watch rules)
(watch facts)
(run)
(save-facts "ger_mrs.dat" visible)
(exit)


	 
