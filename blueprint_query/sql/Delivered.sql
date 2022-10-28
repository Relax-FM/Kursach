select nt.id_N,nt.Date,c.Name,c.Surname,c.Adress,c.Number from lab1.note as nt
              join lab1.client as c on nt.N_client=c.id_C
              where nt.Done=1;