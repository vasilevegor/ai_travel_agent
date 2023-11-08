"use client"; //make for frontend

import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then(res => res.json())
export default function FlightDetailPage ({params}) {
    const {id} = params

    const url = `http://127.0.0.1:8000/flights/${id}`
    const { data, error, isLoading } = useSWR(url, fetcher)

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return <div>{JSON.stringify(data)}</div>
}