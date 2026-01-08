import request from './index'

export const formatJson = (content: string, indent = 2) =>
  request.post('/dev/json/format', { content, indent })

export const compressJson = (content: string) =>
  request.post('/dev/json/compress', { content })

export const validateJson = (content: string) =>
  request.post('/dev/json/validate', { content })

export const base64Encode = (content: string) =>
  request.post('/dev/crypto/base64/encode', { content })

export const base64Decode = (content: string) =>
  request.post('/dev/crypto/base64/decode', { content })

export const md5Hash = (content: string) =>
  request.post('/dev/crypto/md5', { content })

export const shaHash = (content: string, algorithm = 'sha256') =>
  request.post('/dev/crypto/sha', { content, algorithm })

export const timestampConvert = (timestamp?: number, datetime_str?: string) =>
  request.post('/dev/encoding/timestamp', { timestamp, datetime_str })