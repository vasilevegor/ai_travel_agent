"use client"; //make for frontend
import performAPIGetRequest from '@/app/utils/apiClient'

export default function AirportDropdown({name}) {
  const { data, error, isLoading } = performAPIGetRequest("/airports")
  if (error) return <select className='dark: text-blue-400'><option>---Error---</option></select>
  if (isLoading) return <select><option>---Loading---</option></select>
  const displayData = [...data]
  return <select className='dark: text-blue-400' name={name}>
    {displayData.map((airport, idx)=>{
        return <option key={idx} value={airport.value} className='dark: text-blue-400'>({airport.value}) - {airport.label}</option>
    })}
    
  </select>
}