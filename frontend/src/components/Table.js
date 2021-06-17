import React from 'react';
import Table from 'react-bootstrap/Table'
const Tablec = ({ data, columns, title }) => {
    const evalField = (d, type, field) => {
        switch (type) {
            case 'money':
                return `$ ${d[field].replace(/\B(?=(\d{3})+(?!\d))/g, ",")} MXN.`
            case 'tags':
                let tags = ''
                d[field].map(tag => tags += `${tag.name}, `)
                return tags
            default:
                return d[field]


        }
    }

    return (
        <>
            <h1>{title}</h1>
            <br />
            <Table striped bordered hover>
                <thead>
                    <tr>
                        {
                            columns.map(column => {
                                return (
                                    <th key={column.field}>{column.name}</th>
                                )
                            })
                        }
                    </tr>
                </thead>

                <tbody>
                    {data ? data.map(d => {
                        return (
                            <tr key={d.id}>
                                {columns.map(column => {
                                    return (
                                        <td key={`${d.id}-${column.field}`}>
                                            {
                                                evalField(d, column.type, column.field)
                                            }


                                        </td>
                                    )
                                })}

                            </tr>

                        )
                    }) : <tr></tr>}
                </tbody>

            </Table>

        </>
    )

}

export default Tablec;