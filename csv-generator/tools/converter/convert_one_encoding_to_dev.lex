/* Programme to convert Indian languages to devanagiri */
/* Written by Roja (04-04-2015)			       */
/* RUN: ./comp.sh convert_one_encoding_to_dev	       */
/*	./convert_one_encoding_to_dev.out < $1 > output  */
/*******************************************************/

%%
\340\240	{  printf("\340\244"); /*Samaritan*/	}

\340\244	{  ECHO;	}
\340\245	{  ECHO;	}

\340\246	{ printf("\340\244"); /*Bengali*/	}
\340\247	{ printf("\340\245"); /*Bengali*/	}

\340\250	{ printf("\340\244"); /*Punjabi*/	}
\340\251	{ printf("\340\245"); /*Punjabi*/	}

\340\252	{ printf("\340\244"); /*Gujarati*/	}
\340\253	{ printf("\340\245"); /*Gujarati*/	}

\340\254	{ printf("\340\244"); /*Oriya*/		}
\340\255	{ printf("\340\245"); /*Oriya*/		}

\340\256	{ printf("\340\244"); /*Tamil*/		}
\340\257	{ printf("\340\245"); /*Tamil*/		}

\340\260	{ printf("\340\244"); /*Telugu*/	}
\340\261	{ printf("\340\245"); /*Telugu*/	}

\340\262	{ printf("\340\244"); /*Kanada*/	}
\340\263	{ printf("\340\245"); /*Kanada*/	}

\340\264	{ printf("\340\244"); /*Malayalam*/	}
\340\265	{ printf("\340\245"); /*Malayalam*/	}

\340\266	{ printf("\340\244"); /*Sinhala*/	}
\340\267	{ printf("\340\245"); /*Sinhala*/	}

\340\270	{ printf("\340\244"); /*Thai*/		}
\340\271	{ printf("\340\245"); /*Thai*/		}

\340\274	{ printf("\340\244"); /*Tibetan*/	}
\340\275	{ printf("\340\245"); /*Tibetan*/	}

%%

