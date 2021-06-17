import axios from 'axios'
import { useState, useEffect } from 'react'
import Tablec from '../../components/Table'
const Articles = () => {
    const columns = [
        {
            field: 'id',
            name: 'ID'
        },
        {
            field: 'description',
            name: 'Description'
        },
        {
            field: 'code',
            name: 'Code'
        },
        {
            field: 'price',
            name: 'Price',
            type: 'money'
        },
        {
            field: 'vendors_detail',
            name: 'Vendors',
            type: 'tags'
        },
        {
            field: 'created',
            name: 'Created'
        },
    ]
    const [articles, setArticles] = useState({ loading: true })
    useEffect(() => {
        axios.get('/api/v1/articles/article/').then(res => {
            setArticles({ loading: false, data: res.data })
        }).catch(err => {
            setArticles({ loading: false, data: err.details })
        })
    }, [])
    return (
        <>
            {articles.loading
                ? 'Cargando......' :
                <Tablec data={articles.data} columns={columns} title={'Articles'} />
            }
        </>
    )
}

export default Articles
