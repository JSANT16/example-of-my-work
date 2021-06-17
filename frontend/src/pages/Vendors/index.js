import axios from 'axios'
import { useState, useEffect } from 'react'
import Tablec from '../../components/Table'
const Vendors = () => {
    const columns = [
        {
            field: 'id',
            name: 'ID'
        },
        {
            field: 'name',
            name: 'Name'
        },
        {
            field: 'address',
            name: 'Address'
        },
        {
            field: 'created',
            name: 'Created'
        },
    ]
    const [vendors, setVendors] = useState({ loading: true })
    useEffect(() => {
        axios.get('/api/v1/articles/vendor/').then(res => {
            setVendors({ loading: false, data: res.data })
        }).catch(err => {
            setVendors({ loading: false, data: err.details })
        })
    }, [])
    return (
        <>
            {vendors.loading
                ? 'Cargando......' :
                <Tablec data={vendors.data} columns={columns} title={'Vendors'} />
            }
        </>
    )
}

export default Vendors
