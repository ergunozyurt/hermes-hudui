export function withProfile(path: string, profile?: string | null) {
  if (!profile || profile === 'default') return path
  const separator = path.indexOf('?') >= 0 ? '&' : '?'
  return `${path}${separator}profile=${encodeURIComponent(profile)}`
}

export function profileLabel(profile?: string | null) {
  return !profile || profile === 'default' ? 'default' : profile
}

export function profileDisplayName(profile?: string | null) {
  return !profile || profile === 'default' ? 'Hermes' : profile
}