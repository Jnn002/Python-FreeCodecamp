#notas



\d => [01234567890]
El simbolo '^' dentro de un conjutno de caracteres con corchetes  
indica una 'negación', es decir la expresión regular debe coincidir
con cualquier carácter EXCEPTO los especificados en el conjunto
\D => [^01234567890]  => TODOS AQUELLOS VALORES QUE NO SEAN NÚMERICOS

\w => [a-zA-Z0-9_] => alphanumeric characters
\W => {^a-zA-Z0-9_} => Todos los characteres no alphanumericos