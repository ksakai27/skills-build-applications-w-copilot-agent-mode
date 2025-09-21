import React, { useEffect, useState } from 'react'

function getApiBase() {
  const name = process.env.REACT_APP_CODESPACE_NAME
  if (name) return `https://${name}-8000.app.github.dev`
  return 'http://localhost:8000'
}

export default function Teams() {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(false)
  const [selected, setSelected] = useState(null)

  useEffect(() => {
    fetchTeams()
  }, [])

  function fetchTeams() {
    setLoading(true)
    const url = `${getApiBase()}/api/teams/`
    console.log('Teams fetching from', url)
    fetch(url)
      .then(res => res.json())
      .then(json => {
        console.log('Teams fetched raw:', json)
        const result = Array.isArray(json) ? json : (json.results || json)
        console.log('Teams normalized:', result)
        setData(result)
      })
      .catch(err => console.error('Teams fetch error', err))
      .finally(() => setLoading(false))
  }

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h3>Teams</h3>
        <button className="btn btn-sm btn-outline-secondary" onClick={fetchTeams} disabled={loading}>{loading ? 'Loading...' : 'Refresh'}</button>
      </div>

      <div className="card table-card">
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Team</th>
                  <th>Members</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    <td>{idx + 1}</td>
                    <td>{item.name || item.title || ('Team ' + (idx + 1))}</td>
                    <td>{item.members || item.size || '-'}</td>
                    <td><button className="btn btn-sm btn-primary" onClick={() => setSelected(item)}>View</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {selected && (
        <div className="modal show d-block" tabIndex="-1">
          <div className="modal-dialog modal-lg">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Team Details</h5>
                <button type="button" className="btn-close" onClick={() => setSelected(null)} />
              </div>
              <div className="modal-body"><pre>{JSON.stringify(selected, null, 2)}</pre></div>
              <div className="modal-footer"><button className="btn btn-secondary" onClick={() => setSelected(null)}>Close</button></div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
