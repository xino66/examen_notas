import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from "/components/ui/card"
import { Button } from "/components/ui/button"
import { Alert, AlertDescription, AlertTitle } from "/components/ui/alert"
import { Shield } from "lucide-react"

const DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

export default function TemperatureAnalyzer() {
  const [temperatures, setTemperatures] = useState<Record<string, number>>(
    DAYS_OF_WEEK.reduce((acc, day) => ({ ...acc, [day]: 0 }), {})
  )
  const [showResults, setShowResults] = useState(false)

  const handleTemperatureChange = (day: string, value: string) => {
    const numValue = value === '' ? 0 : parseFloat(value)
    setTemperatures(prev => ({ ...prev, [day]: numValue }))
  }

  const temperatureValues = Object.values(temperatures)
  const maxTemp = Math.max(...temperatureValues)
  const minTemp = Math.min(...temperatureValues)
  const avgTemp = temperatureValues.reduce((sum, temp) => sum + temp, 0) / temperatureValues.length
  const daysAboveAvg = DAYS_OF_WEEK.filter(day => temperatures[day] > avgTemp)
  const extremeTemps = DAYS_OF_WEEK.filter(day => 
    temperatures[day] > 40 || temperatures[day] < 0
  )

  const resetForm = () => {
    setTemperatures(DAYS_OF_WEEK.reduce((acc, day) => ({ ...acc, [day]: 0 }), {}))
    setShowResults(false)
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-3xl">
      <Card>
        <CardHeader>
          <CardTitle className="text-2xl font-bold">
            Weekly Temperature Analyzer
          </CardTitle>
        </CardHeader>
        <CardContent>
          {!showResults ? (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold">Enter Daily Temperatures (°C)</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {DAYS_OF_WEEK.map(day => (
                  <div key={day} className="flex items-center space-x-2">
                    <label className="w-24 font-medium">{day}:</label>
                    <input
                      type="number"
                      value={temperatures[day] === 0 ? '' : temperatures[day]}
                      onChange={(e) => handleTemperatureChange(day, e.target.value)}
                      className="border rounded px-3 py-2 w-full"
                      placeholder="Enter temperature"
                    />
                  </div>
                ))}
              </div>
              <div className="flex justify-end space-x-2">
                <Button variant="outline" onClick={resetForm}>
                  Reset
                </Button>
                <Button onClick={() => setShowResults(true)}>
                  Analyze Temperatures
                </Button>
              </div>
            </div>
          ) : (
            <div className="space-y-6">
              <h2 className="text-xl font-bold">Temperature Analysis</h2>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-50 p-4 rounded-lg">
                  <h3 className="font-semibold text-blue-800">Maximum</h3>
                  <p className="text-2xl font-bold">{maxTemp.toFixed(1)}°C</p>
                </div>
                <div className="bg-green-50 p-4 rounded-lg">
                  <h3 className="font-semibold text-green-800">Minimum</h3>
                  <p className="text-2xl font-bold">{minTemp.toFixed(1)}°C</p>
                </div>
                <div className="bg-purple-50 p-4 rounded-lg">
                  <h3 className="font-semibold text-purple-800">Average</h3>
                  <p className="text-2xl font-bold">{avgTemp.toFixed(1)}°C</p>
                </div>
              </div>

              {daysAboveAvg.length > 0 && (
                <div>
                  <h3 className="font-semibold mb-2">Days Above Average:</h3>
                  <div className="flex flex-wrap gap-2">
                    {daysAboveAvg.map(day => (
                      <span key={day} className="bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full">
                        {day} ({temperatures[day].toFixed(1)}°C)
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {extremeTemps.length > 0 && (
                <div>
                  <h3 className="font-semibold mb-2">Extreme Temperature Alerts:</h3>
                  <div className="space-y-2">
                    {extremeTemps.map(day => (
                      <Alert 
                        key={day} 
                        variant={temperatures[day] > 40 ? "destructive" : "default"}
                      >
                        <Shield className="h-4 w-4" />
                        <AlertTitle>
                          {temperatures[day] > 40 ? 'Heat Warning' : 'Freeze Warning'}
                        </AlertTitle>
                        <AlertDescription>
                          {day}: {temperatures[day].toFixed(1)}°C - 
                          {temperatures[day] > 40 
                            ? ' Temperature exceeds 40°C' 
                            : ' Temperature below 0°C'}
                        </AlertDescription>
                      </Alert>
                    ))}
                  </div>
                </div>
              )}

              <div className="flex justify-end">
                <Button variant="outline" onClick={() => setShowResults(false)}>
                  Back to Input
                </Button>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
