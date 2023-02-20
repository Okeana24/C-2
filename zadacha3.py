var x, y, S, P: integer;

begin

   readln(S, P);

   for x := 1 to 1000 do

       for y := 1 to 1000 do

           if (x + y = S) and (x * y = P) then

               writeln(x, ' ', y);