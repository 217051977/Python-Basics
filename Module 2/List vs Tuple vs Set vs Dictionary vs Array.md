| Feature    | List          | Tuple         | Set          | Dictionary     | Array              |
|------------|---------------|---------------|--------------|----------------|--------------------|
| Syntax     | [1, 2]        | (1, 2)        | {1, 2}       | {""a"": 1}     | array('i', [1, 2]) |
| Ordered    | Yes           | Yes           | No           | Yes (3.7+)     | Yes                |
| Mutable    | Yes           | No            | Yes          | Yes            | Yes                |
| Duplicates | Allowed       | Allowed       | Not Allowed  | Keys: No       | Allowed            |
| Access     | Index         | Index         | Membership   | Key            | Index              |
| Best For   | Dynamic lists | Fixed records | Unique items | Key-value maps | Numeric efficiency |