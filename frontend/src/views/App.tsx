import { useState } from 'react'
import { motion } from 'framer-motion'
import axios from 'axios'
import React from 'react'

const API_BASE = 'http://localhost:8000'

export default function App() {
  const [file, setFile] = useState<File | null>(null)
  const [docId, setDocId] = useState<string | null>(null)
  const [evidence, setEvidence] = useState<any | null>(null)

  async function upload() {
    if (!file) return
    const form = new FormData()
    form.append('file', file)
    const res = await axios.post(`${API_BASE}/ingest/upload`, form)
    setDocId(res.data.id)
  }

  async function getEvidence() {
    if (!docId) return
    const res = await axios.get(`${API_BASE}/evidence/card/${docId}`)
    setEvidence(res.data)
  }

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="p-4 shadow bg-white">
        <h1 className="text-xl font-semibold">K-METIS</h1>
      </header>
      <main className="p-6 max-w-5xl mx-auto space-y-6">
        <section className="bg-white p-4 rounded border">
          <h2 className="font-medium mb-2">Upload</h2>
          <input type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
          <button onClick={upload} className="ml-3 px-3 py-1.5 bg-black text-white rounded">Upload</button>
          {docId && <span className="ml-3 text-sm text-gray-600">Doc ID: {docId}</span>}
        </section>
        <section className="bg-white p-4 rounded border">
          <h2 className="font-medium mb-2">Evidence Card</h2>
          <button onClick={getEvidence} className="px-3 py-1.5 bg-blue-600 text-white rounded">Fetch</button>
          {evidence && (
            <motion.pre initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mt-3 bg-gray-100 p-3 rounded text-sm overflow-auto">
              {JSON.stringify(evidence, null, 2)}
            </motion.pre>
          )}
        </section>
      </main>
    </div>
  )
}


