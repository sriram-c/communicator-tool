### Added by Roja(08-03-17)
### Program to check the existence of prep clp file in prep_rules.
### If a clp file exists then its copied to provisional prep directory.
MYPATH=`pwd`
var=${MYPATH/%prep_prov_rules/}

cd $var/prep_rules 

if  [ -e  $1.clp ] ; then 
  if [ -e $MYPATH/$1.clp ] ; then    
 	echo "$1.clp already exists in your $MYPATH folder"
  else
	echo "$1.clp already exists in prep_rules folder so copying in $MYPATH folder"	
        sed -e 's/?\*prep_path\*/?\*prep_prov_path\*/g' $1.clp > $MYPATH/$1.clp 
  fi
else
  if [ -e $MYPATH/$1.clp ] ; then    
 	echo "$1.clp already exists in your $MYPATH folder"
  else
  	echo "$1.clp does not exists"
  fi
fi
