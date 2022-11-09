select n.id_N, n.Date, n.N_client, n_n.Mass, n_n.`Col-vo`, n_s.Name from lab1.note as n
join lab1.note_note as n_n on n.id_N = n_n.N_N_Note
join lab1.note_stock as n_s on n_n.N_N_Stock = n_s.id_N_S where n.id_N = '$input_product';