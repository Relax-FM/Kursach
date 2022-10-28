select n_s.id_N_S,nt.Date,n_s.Name,n_n.`Col-vo`,n_n.Mass from lab1.note as nt
              join lab1.note_note as n_n on nt.id_n=n_n.N_N_Note
                        join lab1.note_stock as n_s on n_n.N_N_Stock=n_s.id_N_S
              where id_N='$input_product';