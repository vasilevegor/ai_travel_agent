"use client"; //make for frontend

import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function Home() {
  const url = "http://127.0.0.1:8000/flights"
  const { data, error, isLoading } = useSWR(url, fetcher)
  const mainClassCSS = "flex min-h-screen flex-col items-center justify-between p-24"
  const linkCSS = "text-blue-500 hover:text-blue-900"
 
  if (error) return <div className={mainClassCSS}>failed to load</div>
  if (isLoading) return <div className={mainClassCSS}>loading...</div>
  console.log(data)
  const renderListData = (row, idx) => {
    const flightRowLink = `/flights/${row.id}`
    return <div key={`flight-data-${idx}`}>
      <p>
        <a className={linkCSS} href={flightRowLink}>{row.flightDate}</a>
      </p>
      <p>
        {row.startingAirport}
      </p>
      <p>
        {row.destinationAirport}
      </p>
      <p>
        {row.totalFare}
      </p>
    </div>
  }
  return (// jsx
    <main className={mainClassCSS}>
      <h1>Hello world!</h1>
      {data && data.map(renderListData)}
    </main>
  )
}
