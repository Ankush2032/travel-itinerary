from csv_operations import save_to_csv, read_csv_to_dict_list

rows  = read_csv_to_dict_list('Top Indian Places to Visit.csv').append(read_csv_to_dict_list('multiple_hotels_per_name_full.csv'))
done = []
_id = 0

for row in rows:
    if row['City'] not in done:
        data_ = {
            'id' : _id,
            'City': row['City']
        }
        save_to_csv(data_, 'CitiesSchema.csv')
        _id += 1


